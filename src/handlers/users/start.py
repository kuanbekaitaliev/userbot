from aiogram import Router, types
from aiogram.filters import Command

from db.query import exist_user
from keyboards.inline.menu import menu_kb
from keyboards.inline.lang import start_lang_kb

router = Router()


@router.message(Command("start"))
async def start_msg_handler(msg: types.Message):
    user = await exist_user(tg_userid=msg.from_user.id)
    if not user:
        await msg.answer(text='Выберите язык интерфейса', reply_markup=start_lang_kb())
    else:
        template_msg = [
            "Шаблонное приветствие\n",
            "Поменяй меня на другой текст\n",
            "Исходники - https://github.com/zhandos256/templateaiogram\n",
        ]
        await msg.answer(text="\n".join(template_msg), reply_markup=menu_kb())
