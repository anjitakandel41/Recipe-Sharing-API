import logging
import mimetypes
import re
from email.message import MIMEPart

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import Recipe

logger = logging.getLogger(__name__)

PHOTO_CID = "recipe-photo"

# Leading bullets / numbering that authors often paste in with their text.
BULLET_RE = re.compile(r"^\s*(?:[-*•‣●▪]|\d+[.)])\s*")


def split_items(text):
    """Turn a free-form ingredients/steps blob into a clean list of items."""
    if not text:
        return []

    lines = [line.strip() for line in text.replace("\r\n", "\n").split("\n")]
    items = [line for line in lines if line]

    # Single-line input is usually comma separated ("flour, sugar, 2 eggs").
    if len(items) == 1 and "," in items[0]:
        items = [part.strip() for part in items[0].split(",") if part.strip()]

    return [BULLET_RE.sub("", item) for item in items]


def format_cooking_time(minutes):
    """Render 90 as '1 hr 30 min' and 45 as '45 min'."""
    if not minutes:
        return "Not specified"

    hours, mins = divmod(int(minutes), 60)
    if hours and mins:
        return f"{hours} hr {mins} min"
    if hours:
        return f"{hours} hr"
    return f"{mins} min"


def read_photo(recipe):
    """Return (filename, bytes, mimetype) for the recipe photo, or None."""
    if not recipe.photo:
        return None

    try:
        recipe.photo.open("rb")
        try:
            content = recipe.photo.read()
        finally:
            recipe.photo.close()
    except (FileNotFoundError, OSError, ValueError):
        logger.warning("Recipe %s: photo could not be read.", recipe.pk, exc_info=True)
        return None

    if not content:
        return None

    filename = recipe.photo.name.rsplit("/", 1)[-1]
    mimetype = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    if not mimetype.startswith("image/"):
        mimetype = "image/jpeg"

    return filename, content, mimetype


def build_inline_image(filename, content, mimetype):
    """Build an inline (Content-ID) image part the HTML body can reference."""
    subtype = mimetype.split("/", 1)[1]
    part = MIMEPart()
    part.set_content(
        content,
        maintype="image",
        subtype=subtype,
        cid=f"<{PHOTO_CID}>",
        disposition="inline",
        filename=filename,
    )
    return part


def build_recipe_email(recipe):
    """Build the 'recipe published' email: HTML + plain text + inline photo."""
    photo = read_photo(recipe)
    author = recipe.author

    context = {
        "recipe": recipe,
        "site_name": getattr(settings, "SITE_NAME", "Recipe Sharing API"),
        "author_name": author.get_full_name() or author.username,
        "category_name": recipe.category.name if recipe.category_id else "Uncategorized",
        "cooking_time_display": format_cooking_time(recipe.cooking_time),
        "ingredients": split_items(recipe.ingredients),
        "steps": split_items(recipe.steps),
        "has_photo": photo is not None,
        "photo_cid": PHOTO_CID,
        "separator": "=" * len(recipe.title),
    }

    text_body = render_to_string("recipes/email/recipe_published.txt", context)
    html_body = render_to_string("recipes/email/recipe_published.html", context)

    message = EmailMultiAlternatives(
        subject=f"Your recipe is live: {recipe.title}",
        body=text_body,
        from_email=settings.DEFAULT_FROM_EMAIL or None,
        to=[author.email],
    )
    message.attach_alternative(html_body, "text/html")

    if photo:
        message.attach(build_inline_image(*photo))

    return message


@receiver(post_save, sender=Recipe)
def send_recipe_email(sender, instance, created, **kwargs):
    if not created or not instance.author.email:
        return

    try:
        build_recipe_email(instance).send(fail_silently=False)
    except Exception:
        # Never let a mail failure break the API request that created the recipe.
        logger.exception("Failed to send recipe email for recipe %s.", instance.pk)
