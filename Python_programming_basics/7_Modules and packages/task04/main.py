import platform
import speedtest

# Функция для преобразования бит в мегабайты
def bits_to_megabytes(bits):
    return bits / 8 / 1024 / 1024

# Получаем информацию о системе
system_info = platform.uname()
print("Тип системы:", system_info.system, system_info.release,
      system_info.version)
print("Установленный процессор:", system_info.processor)
print("Текущая версия компилятора: ", system_info.machine)
print("Текущая версия python: ", system_info.version)

# Получаем информацию о скорости интернета
st = speedtest.Speedtest()
download_speed = st.download()
upload_speed = st.upload()

print("Скорость загрузки: ", bits_to_megabytes(download_speed))
print("Скорость отдачи: ", bits_to_megabytes(upload_speed))