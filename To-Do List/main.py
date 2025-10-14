from Task import  Task
from  Todolist import  Todolist



tugas = Task("menyapu kamar")
tugas_2 = Task("menyuci piring")
tugas_3 = Task("belajar", )


todo = Todolist()

todo.add_task(tugas)
todo.add_task(tugas_2)
todo.add_task(tugas_3)

todo.show_all_tasks()
todo.mark_task_done("menyapu kamar")
todo.show_all_tasks()




