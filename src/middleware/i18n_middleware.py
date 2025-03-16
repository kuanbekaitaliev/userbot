from typing import Any, Dict

from aiogram.types import TelegramObject
from aiogram.utils.i18n import I18n, I18nMiddleware

from config.const import LOCALES_DIR, DEFAULT_LOCALE, DOMAIN_MESSAGES
from database.queries import get_user_lang


class CustomI18nMiddleware(I18nMiddleware):
    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        user = data["event_from_user"]
        userid = int(user.id)
        return await get_user_lang(tg_userid=userid) or DEFAULT_LOCALE


i18n = I18n(path=LOCALES_DIR, default_locale=DEFAULT_LOCALE, domain=DOMAIN_MESSAGES)
i18n_middleware = CustomI18nMiddleware(i18n=i18n)
