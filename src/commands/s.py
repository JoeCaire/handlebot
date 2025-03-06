from .ship import ship

async def s_command(message, lang):
    await ship(message, lang)
