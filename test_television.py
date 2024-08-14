# test_television.py
import pytest

class Television:
    def __init__(self, brand, screen_size):
        self.brand = brand
        self.screen_size = screen_size
        self.is_on = False
        self.volume = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def increase_volume(self):
        if self.is_on:
            self.volume += 1

    def decrease_volume(self):
        if self.is_on:
            self.volume -= 1

@pytest.fixture
def television():
    return Television("Samsung", 50)

def test_television_initialization(television):
    assert television.brand == "Samsung"
    assert television.screen_size == 50
    assert not television.is_on
    assert television.volume == 0

def test_turn_on_television(television):
    television.turn_on()
    assert television.is_on

def test_turn_off_television(television):
    television.turn_on()
    television.turn_off()
    assert not television.is_on

def test_increase_volume(television):
    television.turn_on()
    television.increase_volume()
    assert television.volume == 1

def test_decrease_volume(television):
    television.turn_on()
    television.increase_volume()
    television.decrease_volume()
    assert television.volume == 0

def test_cannot_decrease_volume_when_off(television):
    television.turn_off()
    television.decrease_volume()
    assert television.volume == 0

def test_cannot_increase_volume_when_off(television):
    television.turn_off()
    television.increase_volume()
    assert television.volume == 0