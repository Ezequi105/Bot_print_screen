import pyautogui
import time

# Mensagem e tempo de espera
print("Aguardando 5 segundos... prepare a tela para o print!")
time.sleep(5)

# Tira print da tela inteira
screenshot = pyautogui.screenshot()

# Salva o arquivo
screenshot.save("print_tela_completa.png")

print("Print tirado e salvo como 'print_tela_completa.png'")
