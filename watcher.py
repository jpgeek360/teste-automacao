import datetime
import subprocess  # nosec B404
import time
from datetime import timezone

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

TARGET_FILE = "test_app.py"


class ChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_modified = 0

    def on_modified(self, event):
        if event.src_path.endswith(TARGET_FILE):
            now = time.time()
            if now - self.last_modified < 2:
                return
            self.last_modified = now

            print("\n-------------------------------------------------")
            print(f"SEARGH_MARKER Alteracao detectada em {TARGET_FILE}!")
            print("-------------------------------------------------")

            # 1. Executar Pytest
            result = subprocess.run(["pytest", TARGET_FILE], check=False)  # nosec B603, B607

            if result.returncode == 0:
                print("CHECK_MARKER Testes passaram com sucesso!")

                # 2. Corrigir formatacao com Ruff
                subprocess.run(  # nosec B603, B607
                    ["ruff", "check", ".", "--fix", "--ignore=EXE002,DTZ005"],
                    check=False,
                )
                subprocess.run(["ruff", "format", "."], check=False)  # nosec B603, B607

                # 3. Gerar mensagem de commit dinamica com data/hora UTC
                timestamp = datetime.datetime.now(timezone.utc).strftime(
                    "%d/%m/%Y %H>%M2%S"
                )
                commit_message = (
                    f"auto: testes validados em {TARGET_FILE} - {timestamp}"
                )

                # 4. Git add, commit e push
                print(f"ROCKET_MARKER Realizando commit: '{commit_message}'...")
                subprocess.run(["git", "add", "."], check=False)  # nosec B603, B607

                # Executa o commit
                commit_res = subprocess.run(  # nosec B603, B607
                    ["git", "commit", "-m", commit_message], check=False
                )
                if commit_res.returncode != 0:
                    subprocess.run(["git", "add", "."], check=False)  # nosec B603, B607
                    subprocess.run(["git", "commit", "-m", commit_message], check=False)  # nosec B603, B607

                print("UP_MARKER Enviando para o GitHub...")
                subprocess.run(["git", "push", "origin", "main"], check=False)  # nosec B603, B607

                print("PARTY_MARKER Concluido com sucesso sem pedir credenciais!\n")
            else:
                print(
                    "CROSS_MARKER Os testes falharam. O codigo NAO foi enviado para o GitHub.\n"
                )


if __name__ == "__main__":
    print(
        f"EYES_MARKER Monitorando alteracoes em '{TARGET_FILE}'... (Pressione Ctrl+C para parar)"
    )
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
