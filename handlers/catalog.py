from aiogram import F, Router, types

from keyboards.catalog import generate_catalog_kb

router = Router()

CATALOG = {
    'romans': {'text': 'Romans', 'description': 'Romans books'},
    'fantasies': {'text': 'Fantasy', 'description': 'Fantasy books'},
    'horrors': {'text': 'Horror', 'description': 'Horror books'},
    'detectives': {'text': 'Detective', 'description': 'Detective books'},
    'documentaries': {'text': 'Documentary', 'description': 'Documentary books'},
}


@router.callback_query(F.data == 'catalog')
@router.message(F.text == 'Catalog')
async def catalog(update: types.Message | types.CallbackQuery):
    if isinstance(update, types.Message):
        await update.answer(
            'Our catalog:',
            reply_markup=generate_catalog_kb(CATALOG)
        )
    else:
        await update.message.edit_text(
            'Our catalog:',
            reply_markup=generate_catalog_kb(CATALOG)
        )


@router.callback_query(F.data.startswith('category'))
async def catalog_info(callback: types.CallbackQuery):
    category_key = callback.data.split(':')[-1]
    category = CATALOG[category_key]
    await callback.message.edit_text(
        text=category['description'],
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton(
                        text='Back',
                        callback_data='catalog'
                    )
                ]
            ]
        )
    )
