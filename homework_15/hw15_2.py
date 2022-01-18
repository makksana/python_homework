print('Task 2', end='\n\n')

# Implement 2 classes,
# the first one is the Boss and
# the second one is the Worker.

# Worker has a property 'boss',
# and its value must be an instance of Boss.

# You can reassign this value,
# but you should check
# whether the new value is Boss.
# Each Boss has a list of his own workers.
# You should implement a method
# that allows you to add workers to a Boss.
# You're not allowed to add
# instances of Boss's class to workers list directly
# via access to attribute,
# use getters and setters instead!

# You can refactor the existing code.
# id_ - is just a random unique integer


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.__workers = []

    @property
    def workers(self):
        return self.__workers

    @workers.setter
    def workers(self, new_worker):
        self.__workers.append(new_worker)

    def hire(self, new_worker):
        if new_worker not in self.workers:
            print(f'Worker {new_worker.name} was hired by {self.name}')
            # Add new worker to the list of workers
            self.workers = new_worker
            # Assign current boss to the new_worker
            new_worker.boss = self
            new_worker.company = self.company

    def fire(self, old_worker):
        for index, worker in enumerate(self.workers):
            if worker.id == old_worker.id:
                print(f'Worker {old_worker.name} was fired by {self.name}')
                del self.workers[index]
                old_worker.company = None
                del old_worker.boss

    def __str__(self) -> str:
        all_workers = [worker.name for worker in self.workers]
        return f'Boss #{self.id} {self.name} works at {self.company} managing {all_workers}'


class Worker:
    def __init__(self, id_: int, name: str):
        self.id = id_
        self.name = name
        self.company = None
        self.__boss = None

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, new_boss: Boss):
        if isinstance(new_boss, Boss):
            self.__boss = new_boss

    @boss.deleter
    def boss(self):
        self.__boss = None

    def __str__(self) -> str:
        if self.boss != None:
            tmp_boss = self.boss.name
        else:
            tmp_boss = 'none'
        return f'Worker #{self.id} {self.name} works at {self.company} and his/her boss: {tmp_boss}'


boss1 = Boss(1, 'Dick', 'facebook')
print(boss1)
boss2 = Boss(2, 'Jerk', 'google')
print(boss2)
worker1 = Worker(1, 'Angel')
worker2 = Worker(2, 'David')
print(worker1)
print(worker2)
boss1.hire(worker1)
boss1.hire(worker2)
print(boss1)
print(worker1)
print(worker2)
boss1.fire(worker1)
print(boss1)
print(worker1)
boss2.hire(worker1)
print(boss2)
print(worker1)
