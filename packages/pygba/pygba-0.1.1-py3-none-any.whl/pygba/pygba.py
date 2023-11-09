import mgba.core

from pygba.utils import KEY_MAP


class PyGBA:
    @staticmethod
    def load(gba_file: str, autoload_save: bool = False) -> "PyGBA":
        core = mgba.core.load_path(gba_file)
        if autoload_save:
            core.autoload_save()
        core.reset()
        return PyGBA(core)
    
    def __init__(self, core: mgba.core.Core):
        self.core = core

    def wait(self, frames: int):
        for _ in range(frames):
            self.core.run_frame()

    def press_key(self, key: str, frames: int = 2):
        if key not in KEY_MAP:
            raise ValueError(f"Invalid key: {key}")
        if frames < 2:
            raise ValueError("Cannot press a key for less than 2 frames.")
        
        key = KEY_MAP[key]
        self.core.add_keys(key)
        self.wait(frames - 1)
        self.core.clear_keys(key)
        self.wait(1)

    def press_up(self, frames: int = 2):
        self.press_key("up", frames)

    def press_down(self, frames: int = 2):
        self.press_key("down", frames)

    def press_left(self, frames: int = 2):
        self.press_key("left", frames)

    def press_right(self, frames: int = 2):
        self.press_key("right", frames)

    def press_a(self, frames: int = 2):
        self.press_key("A", frames)

    def press_b(self, frames: int = 2):
        self.press_key("B", frames)

    def press_l(self, frames: int = 2):
        self.press_key("L", frames)

    def press_r(self, frames: int = 2):
        self.press_key("R", frames)

    def press_start(self, frames: int = 2):
        self.press_key("start", frames)

    def press_select(self, frames: int = 2):
        self.press_key("select", frames)

    def read_memory(self, address: int, size: int = 1):
        return self.core.memory[address:address + size]
    def read_u8(self, address: int):
        return self.core.memory[address]
    def read_u16(self, address: int):
        return self.core.memory.u16[address]
    def read_u32(self, address: int):
        return self.core.memory.u32[address]
