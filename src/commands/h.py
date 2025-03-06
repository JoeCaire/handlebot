from .handle import handle

async def h_command(message, lang):
    await handle(message, lang)
