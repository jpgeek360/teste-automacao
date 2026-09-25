import subprocess
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

TARGET_FILE = "test_app.py"


class ChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_modified = 0

    def on_modified(self, event):
        # Evita disparos duplicados em um curto intervalo
        if event.src_path.endswith(TARGET_FILE):
            now = time.time()
            if now - self.last_modified < 2:
                return
            self.last_modified = now

            print("\n------------------------------------------------")
            print(f"🔍 Alteração detectada em {TARGET_FILE}!")
            print("------------------------------------------------")

            # 1. Executar Pytest
            result = subprocess.run(["pytest", TARGET_FILE])

            if result.returncode == 0:
                print("✅ Testes passaram com sucesso!")

                # 2. Corrigir formatação
                subprocess.run(["ruff", "check", ".", "--fix", "--ignore=EXE002"])

                # 3. Git commit e push
                print("🚀 Enviando para o GitHub...")
                subprocess.run(["git", "add", "."])
                subprocess.run(
                    [
                        "git",
                        "commit",
                        "-m",
                        "auto: testes atualizados e validados com sucesso",
                    ]
                )
                subprocess.run(["git", "push", "origin", "main"])

                print("🎉 Processo concluído! O Render atualizará em breve.\n")
            else:
                print(
                    "❌ Os testes falharam. O código NÃO foi enviado para o GitHub.\n"
                )


if __name__ == "__main__":
    print(
        f"👀 Monitorando alterações no arquivo '{TARGET_FILE}'... (Pressione Ctrl+C para parar)"
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
