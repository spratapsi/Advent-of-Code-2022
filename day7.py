from dataclasses import dataclass
from typing import Type

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = dict()
        self.files = dict()
        self.size = 0

    def add_file(self, file):
        self.files[file.name] = file
        self.update_size(file.size)

    def add_subdir(self, newdir):
        self.children[newdir.name] = newdir
        self.update_size(newdir.size)

    def update_size(self, size):
        self.size += size
        if self.parent is not None:
            self.parent.update_size(size)

    def all_subdirs(self):
        yield self
        for sub in self.children.values():
            yield from sub.all_subdirs()

@dataclass
class File:
    name: str
    size: int

root = Directory('')
class Shell:
    def __init__(self):
        self.wd = root

    def mkdir(self, name):
        if name in self.wd.children:
            return
        new_dir = Directory(name, parent=self.wd)
        self.wd.add_subdir(new_dir)

    def cd(self, name):
        if name == '..':
            self.wd = self.wd.parent
        else:
            self.wd = self.wd.children[name]

    def mkfile(self, name, size):
        new_file = File(name, size)
        self.wd.add_file(new_file)



commands = []
with open('day7.in') as file:
    file = iter(file)
    next(file)
    for line in file:
        commands.append(line.strip().split())


shell = Shell()
for command in commands:
    match command:
        case '$', 'cd', dirname:
            shell.cd(dirname)
        case '$', 'ls':
            pass
        case 'dir', dirname:
            shell.mkdir(dirname)
        case size, filename:
            shell.mkfile(filename, int(size))
        case x:
            print(x)


part1 = sum(dir.size for dir in root.all_subdirs() if dir.size <= 100000)
part2 = min(dir.size for dir in root.all_subdirs() if dir.size >= 30000000 - (70000000 - root.size))
print('Part 1:', part1)
print('Part 2:', part2)
