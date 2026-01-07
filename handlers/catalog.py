from aiogram import F, Router, types

from keyboards.catalog import generate_catalog_kb

router = Router()

CATALOG = {
    'romans': {'text': 'Romans'},
    'fantasies': {'text': 'Fantasy'},
    'horrors': {'text': 'Horror'},
    'detectives': {'text': 'Detective'},
    'documentaries': {'text': 'Documentary'},
}

@router.message(F.text == 'Catalog')
async def catalog(message: types.Message):
    await message.answer(
        'Our catalog:',
        reply_markup=generate_catalog_kb(CATALOG)
    )