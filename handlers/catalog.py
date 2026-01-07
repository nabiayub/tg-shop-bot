from aiogram import F, Router, types

router = Router()

@router.message(F.text == 'Catalog')
async def catalog(message: types.Message):
    await message.answer(
        'Our catalog:',
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[
                [types.InlineKeyboardButton(text='Test', callback_data='1')]
            ]
        )
    )