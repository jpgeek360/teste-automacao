import datetime
import subprocess
import time

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

            print("\n------------------------------------------------")
            print(f"🔍 Alteração detectada em {TARGET_FILE}!")
            print("------------------------------------------------")

            # 1. Executar Pytest
            result = subprocess.run(["pytest", TARGET_FILE], check=False)

            if result.returncode == 0:
                print("✅ Testes passaram com sucesso!")

                # 2. Corrigir formatação com Ruff
                subprocess.run(
                    ["ruff", "check", ".", "--fix", "--ignore=EXE002"],
                    check=False,
                )
                subprocess.run(["ruff", "format", "."], check=False)

                # 3. Gerar mensagem de commit dinâmica com data/hora
                timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                commit_message = (
                    f"auto: testes validados em {TARGET_FILE} - {timestamp}"
                )

                # 4. Git add, commit e push
                print(f"🚀 Realizando commit: '{commit_message}'...")
                subprocess.run(["git", "add", "."], check=False)

                # Executa o commit (se o pre-commit reformatar arquivos, tenta o commit novamente)
                commit_res = subprocess.run(
                    ["git", "commit", "-m", commit_message], check=False
                )
                if commit_res.returncode != 0:
                    subprocess.run(["git", "add", "."], check=False)
                    subprocess.run(["git", "commit", "-m", commit_message], check=False)

                print("⬆️ Enviando para o GitHub...")
                subprocess.run(["git", "push", "origin", "main"], check=False)

                print("🎉 Concluído com sucesso sem pedir credenciais!\n")
            else:
                print(
                    "❌ Os testes falharam. O código NÃO foi enviado para o GitHub.\n"
                )


if __name__ == "__main__":
    print(
        f"👀 Monitorando alterações em '{TARGET_FILE}'... (Pressione Ctrl+C para parar)"
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
