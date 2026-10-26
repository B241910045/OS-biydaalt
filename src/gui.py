"""
gui.py - Цонх, товчлуур, оролтын талбар (Гишүүн 4-ийн ажил)

Ажиллуулах:
    python src/gui.py        (Windows)
    python3 src/gui.py       (Linux. Хэрэв tkinter алдаа гарвал: sudo apt install python3-tk)

Зургийг gui_canvas.py-ийн draw_memory() зурна (Гишүүн 3). Энд зөвхөн цонх,
товчлуур, оролтыг хийж, allocator-ийг дуудаад дараа нь зургийг шинэчилнэ.
"""
import tkinter as tk
from tkinter import messagebox

from allocator import Allocator
from gui_canvas import draw_memory


class App:
    def __init__(self, root):
        self.root = root
        root.title("Contiguous Memory Allocation")
        self.allocator = None            # "Эхлүүлэх" дарсны дараа үүснэ
        self.build_widgets()

    def build_widgets(self):
        """Цонхны бүх хэсгийг үүсгэнэ."""
        # --- 1. Санах ойн хэмжээ оруулах мөр (бэлэн) ---
        top = tk.Frame(self.root)
        top.pack(fill="x", padx=10, pady=5)
        tk.Label(top, text="Санах ойн хэмжээ:").pack(side="left")
        self.size_entry = tk.Entry(top, width=12)
        self.size_entry.insert(0, "1000")
        self.size_entry.pack(side="left", padx=5)
        tk.Button(top, text="Эхлүүлэх / Reset", command=self.on_start).pack(side="left")

        # --- 2. Зураг (бэлэн) ---
        self.canvas = tk.Canvas(self.root, width=800, height=150, bg="white")
        self.canvas.pack(padx=10, pady=5)

        # --- 3. Мессеж харуулах мөр (бэлэн) ---
        self.message_var = tk.StringVar()
        tk.Label(self.root, textvariable=self.message_var, fg="blue").pack(pady=2)

        # TODO 1: Хүсэлтийн мөр: процессын нэр (Entry), хэмжээ (Entry),
        #         стратеги (F/B/W - Radiobutton эсвэл OptionMenu), "RQ" товч -> self.on_request
        # TODO 2: Чөлөөлөх мөр: процессын нэр (Entry), "RL" товч -> self.on_release
        # TODO 3: "C (Compaction)" товч -> self.on_compact
        # TODO 4: Статистик харуулах Label (нийт, ашигласан, чөлөөт, hole-ын тоо,
        #         хамгийн том hole, fragmentation %) -> self.refresh() дотор шинэчилнэ

    def on_start(self):
        """Санах ойг эхлүүлэх эсвэл reset хийх."""
        try:
            size = int(self.size_entry.get())
            self.allocator = Allocator(size)
        except ValueError:
            messagebox.showerror("Алдаа", "Санах ойн хэмжээ 0-ээс их бүхэл тоо байх ёстой")
            return
        self.message_var.set("Санах ой " + str(size) + " нэгжээр эхэллээ")
        self.refresh()

    def on_request(self):
        """RQ товч дарахад. TODO: оролтыг уншиж, allocator.request() дуудаад,
        мессеж харуулж, self.refresh() дуудна. Allocator эхлээгүй бол алдаа үзүүлнэ."""
        pass

    def on_release(self):
        """RL товч дарахад. TODO: allocator.release() дуудна."""
        pass

    def on_compact(self):
        """C товч дарахад. TODO: allocator.compact() дуудна."""
        pass

    def refresh(self):
        """Зураг болон статистикийг шинэчилнэ. Allocator-ийн ямар ч өөрчлөлтийн дараа дуудна."""
        if self.allocator is None:
            return
        draw_memory(self.canvas, self.allocator.get_blocks(), self.allocator.max_size)
        # TODO: статистикийн Label-ийг self.allocator.get_stats()-ээр шинэчилнэ


def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
