"""
cli.py - Командын мөрийн интерфейс (Гишүүн 2-ын ажил)

Ажиллуулах:
    python src/cli.py 1048576        (Windows)
    python3 src/cli.py 1048576       (Linux)

Дараа нь   allocator>   гэсэн prompt гарч, дараах командуудыг хүлээн авна:
    RQ P0 40000 W    санах ой хүсэх (F / B / W)
    RL P0            санах ой чөлөөлөх
    C                compaction
    STAT             байдлыг харуулах
    X                гарах

ДҮРЭМ: санах ой хуваарилах логикийг ЭНД БИЧИХГҮЙ. allocator.py-ийн функцийг
дуудаж, үр дүнг нь хэвлэнэ. (allocator.py-г өөрчлөх хэрэггүй)
"""
import sys
from allocator import Allocator

PROMPT = "allocator> "


def format_status(allocator):
    """STAT командын гаралтыг нэг текст болгож буцаана (print хийхгүй).

    Хүссэн гаралт (номын формат):
        Addresses [0:315000] Process P1
        Addresses [315001:512500] Unused
        ...
    Алхам:
      1. blocks = allocator.get_blocks()
      2. block бүрийн хувьд:  "Addresses [" + эхлэх + ":" + төгсөх + "] " + ...
         - эхлэх = block.start,  төгсөх = block.end()
         - block.is_hole() үнэн бол "Unused", үгүй бол "Process " + block.owner
      3. мөрүүдийг "\n"-ээр залгаж буцаана
    """
    # TODO: энд бичнэ
    return ""


def handle_command(allocator, line):
    """Нэг мөр командыг боловсруулна.
    Буцаах утга:  (хэвлэх текст, гарах эсэх)
    Жишээ:  ("P0-д [0:39999] олгов", False)   эсвэл   ("", True)  <- X команд

    Алхам:
      1. parts = line.split()   (мөрийг үгсэд хуваана)
      2. parts хоосон бол ("", False) буцаана
      3. command = parts[0].upper()
      4. command-аас хамаарч:
         "RQ"   -> parts яг 4 үгтэй эсэхийг шалгана (RQ нэр хэмжээ стратеги).
                   хэмжээг int()-д хөрвүүлнэ (try/except ValueError ашиглана,
                   буруу бол "Алдаа: хэмжээ бүхэл тоо байх ёстой").
                   allocator.request(нэр, хэмжээ, стратеги) дуудаж мессежийг буцаана
         "RL"   -> parts яг 2 үгтэй эсэхийг шалгана. allocator.release(нэр)
         "C"    -> allocator.compact()
         "STAT" -> format_status(allocator)
         "X"    -> ("", True)
         бусад  -> ("Алдаа: үл мэдэгдэх команд ...", False)
      5. Аргументын тоо буруу бол хэрэглэх жишээг хэлнэ: "Хэрэглээ: RQ <нэр> <хэмжээ> <F|B|W>"
    """
    # TODO: энд бичнэ
    return "", False


def main():
    """Программын эхлэл. (Энэ хэсэг бэлэн, Гишүүн 2 ойлгоод шаардлагатай бол сайжруулна)"""
    # 1. Аргументыг шалгах
    if len(sys.argv) != 2:
        print("Хэрэглээ: python src/cli.py <санах ойн хэмжээ>")
        return
    try:
        max_size = int(sys.argv[1])
        allocator = Allocator(max_size)
    except ValueError:
        print("Алдаа: санах ойн хэмжээ 0-ээс их бүхэл тоо байх ёстой")
        return

    # 2. Командыг давтан уншина
    while True:
        try:
            line = input(PROMPT)
        except EOFError:
            break          # файлаас уншиж дууссан үед (python src/cli.py 1000 < файл.txt)
        text, should_exit = handle_command(allocator, line)
        if text != "":
            print(text)
        if should_exit:
            break


if __name__ == "__main__":
    main()
