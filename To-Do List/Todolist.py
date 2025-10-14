class Todolist:
    def __init__(self):
        self.tasks = []


    def add_task(self, task):
        self.tasks.append(task)

    def show_all_tasks(self):
        nomor = 0
        print(f"Semua tugas:")
        for task in self.tasks:
            nomor += 1
            print(f"{nomor}.{task.show_task()}")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"tugas {title} berhasil dihapus")
        print(f"tugas {title} tidak ditemukan")



    def mark_task_done(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_done()

    def mark_task_undone(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_undone()