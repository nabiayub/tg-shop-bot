from aiogram import F, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from database import User
from keyboards import profile as profile_kb
from repositories.user import UserRepo
from states.profile import UserDepositState

router = Router()


@router.message(F.text == 'Profile')
async def user_profile_info(
        message: types.Message,
        user_repo: UserRepo,
):
    user: User = await user_repo.get_user_by_tg_id(message.from_user.id)

    await message.answer(
        f'<b>{message.from_user.full_name}</b>\n\n'
        f'Username: {user.username or '-'}\n'
        f'ID: <code>{user.tg_id}</code>\n'
        f'Balance: {user.get_balance} dollars\n',
        parse_mode=ParseMode.HTML,
        reply_markup=profile_kb.profile_menu_kb()
    )


@router.callback_query(F.data == 'deposit')
async def top_up_deposit(
        callback_query: types.CallbackQuery,
        state: FSMContext,
):
    await callback_query.answer()
    await callback_query.message.edit_text(
        'Enter amount to deposit: ',
        reply_markup=profile_kb.break_action_and_back_to_ptofile_kb('Cancel')
    )
    await state.set_state(UserDepositState.INPUT_AMOUNT)

@router.callback_query(StateFilter(UserDepositState), F.data == 'cancel_deposit')
async def cancel_deposit(
        callback_query: types.CallbackQuery,
        state: FSMContext,
        user_repo: UserRepo,
):
    await state.clear()
    await callback_query.answer()

    user: User = await user_repo.get_user_by_tg_id(callback_query.from_user.id)

    await callback_query.message.edit_text(
        f'<b>{callback_query.from_user.full_name}</b>\n\n'
        f'Username: {user.username or '-'}\n'
        f'ID: <code>{user.tg_id}</code>\n'
        f'Balance: {user.get_balance} dollars\n',
        parse_mode=ParseMode.HTML,
        reply_markup=profile_kb.profile_menu_kb()
    )


@router.message(UserDepositState.INPUT_AMOUNT)
async def user_deposit_amount(
        message: types.Message,
        state: FSMContext,
):
    if not message.text.isdigit():
        await message.answer('Enter a integer:')
        return

    amount = int(message.text)

    await state.set_data({'amount': amount})
    await message.answer(
        text=f'“Do you confirm the balance top-up for {amount} dollars?',
        reply_markup=profile_kb.apply_deposit_action_kb()
    )

    await state.set_state(UserDepositState.APPLY_DEPOSIT)


@router.callback_query(UserDepositState.APPLY_DEPOSIT)
async def apply_deposit(
        callback_query: types.CallbackQuery,
        state: FSMContext,
        user_repo: UserRepo,
):
    state_data = await state.get_data()
    deposit_amount = state_data.get('amount')

    await user_repo.update_balance(
        callback_query.from_user.id,
        deposit_amount * 100
    )
    await callback_query.message.edit_text(
        f'Balance is successfully  topped up by {deposit_amount} dollars.',
        reply_markup=profile_kb.break_action_and_back_to_ptofile_kb('Back to Profile')
    )

    await callback_query.answer()
