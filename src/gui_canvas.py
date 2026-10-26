"""
gui_canvas.py - Memory layout-ийг ЗУРАХ хэсэг (Гишүүн 3-ын ажил)

Энэ файл зөвхөн ЗУРАХ ажил хийнэ. Товчлуур, оролтын талбар энд байхгүй
(тэдгээр нь gui.py буюу Гишүүн 4-ийн ажил).

Гишүүн 4 энэ файлын draw_memory() функцийг ингэж дуудна:
    draw_memory(canvas, allocator.get_blocks(), allocator.max_size)
Тиймээс функцийн НЭР, АРГУМЕНТЫГ ӨӨРЧЛӨХГҮЙ байх. Дотор нь хүссэнээрээ сайжруулна.

Одоо байгаа нь хамгийн энгийн ажилладаг хувилбар. Үүнийг сайжруулна (доорх TODO).
"""

HOLE_COLOR = "#d9d9d9"          # hole-ын өнгө (саарал)
PROCESS_COLORS = ["#e6194b", "#3cb44b", "#4363d8", "#f58231", "#911eb4",
                  "#42d4f4", "#f032e6", "#bfef45", "#fabed4", "#469990"]
MARGIN = 20                      # зургийн захын зай


def color_for(name):
    """Процессын нэрээр өнгө сонгоно."""
    total = 0
    for ch in name:
        total = total + ord(ch)
    return PROCESS_COLORS[total % len(PROCESS_COLORS)]


def draw_memory(canvas, blocks, max_size):
    """Санах ойг тэгш өнцөгт мөр хэлбэрээр зурна.
    canvas   : tkinter Canvas
    blocks   : allocator.get_blocks()-ийн үр дүн (Block-уудын жагсаалт)
    max_size : нийт санах ойн хэмжээ
    """
    canvas.delete("all")                      # өмнөх зургийг арилгана
    width = canvas.winfo_width()
    if width < 100:
        width = 800                           # цонх хараахан зурагдаагүй үед
    usable = width - 2 * MARGIN
    top = 40
    bottom = 110

    for block in blocks:
        x1 = MARGIN + block.start * usable / max_size
        x2 = MARGIN + (block.start + block.size) * usable / max_size
        if block.is_hole():
            color = HOLE_COLOR
            label = "hole"
        else:
            color = color_for(block.owner)
            label = block.owner
        canvas.create_rectangle(x1, top, x2, bottom, fill=color, outline="black")
        if x2 - x1 > 40:                      # хангалттай өргөн бол нэр бичнэ
            canvas.create_text((x1 + x2) / 2, (top + bottom) / 2,
                               text=label + "\n" + str(block.size))

    # TODO 1: блок бүрийн эхлэх хаягийг доор нь бичих (0, 200, 500 ...)
    # TODO 2: draw_legend() функц бичиж дуудах (өнгөний тайлбар: процесс, hole)
    # TODO 3: нарийхан блокийн нэр дээр багтахгүй бол жижиг бичих эсвэл алгасах
    # TODO 4: өнгө давхцахгүйгээр өөр өөр процесст өөр өнгө өгөх (color_for-г сайжруулах)
    # TODO 5: fragmentation-ийг харуулах (жишээ нь hole-уудыг хээтэй/хүрээтэй зурах)
    # TODO 6: нэгжийг (byte, KB гэх мэт) зургийн гарчигт бичих
