class Task:
    def __init__(self, judul_tugas):
        self.title = judul_tugas
        self.status = False


    def mark_done(self):
        self.status = True


    def mark_undone(self):
        self.status = False

    def show_task(self):
        # karena self.status bernilai false maka 'if' itu dilewatkan
        if self.status:
            status_text = "selesai"
        else:
            status_text = "belum selesai"
        return f"Tugas kamu: {self.title} - Status: {status_text}"