from aiogram import F, Router, types

from keyboards.inline.settings import settings_kg

router = Router()


@router.callback_query(F.data == "settings")
async def settings_cb(call: types.CallbackQuery):
    await call.message.edit_text(
        text="Настройки бота", reply_markup=await settings_kg()
    )
