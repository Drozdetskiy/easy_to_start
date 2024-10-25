# Этот файл - это точка входа в твою программу
# почитай то что написано в файле src/app/v1/app.py чтобы понять про библиотеки
# и их импорт. Библиотеки это сторонний код который уже написан и его ты
# устанавливаешь чтобы пользоваться тем, что написали другие разработчики
# до тебя
from typer import Typer

# Импортируем две функции run_app - которая все запустит и set_app которая
# создаст нужные объекты для выполнения программы
from app.api.app import (
    run_app as run_external_app,
    set_app,
)

# переменная которая хранит вспомогательный текст
common_help = (
    "Easy to Start service management point. "
    "All commands provided with hyphens as a separators. "
    "All service parts and manual commands are provided from this point."
)


# Переменная которая будет хранить экземпляр объекта Typer.
# он нужен чтобы ты мог запускать свою программу из консоли
cli = Typer(
    help=common_help,
    pretty_exceptions_enable=False,
    pretty_exceptions_show_locals=False,
    pretty_exceptions_short=False,
)


# Создаем функцию для запуска сервера
# @cli.command - помечает для Typer что эта функция является консольной
# командой
# Теперь когда ты сделаешь python manage.py run-http из консоли
# она программа знает что нужно вызвать эту функцию
@cli.command()
def run_http() -> None:
    """Serve external API via HTTP service"""

    # выполняем функцию set_app() которая создает нужные объекты
    set_app()
    # запускаем наш сервер
    run_external_app()


# Это способ описания входной точки для твоей программы
if __name__ == "__main__":
    """Entry point of the application."""

    cli()
