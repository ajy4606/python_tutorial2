# 메소드

class Unit:
    def __init__(self, name, hp): # __init__ 파이썬에서 만들어지는 생성자
        self.name = name
        self.hp = hp

class AttackUnit(Unit): # Unit 상속
     def __init__(self, name, hp, damage): # __init__ 파이썬에서 만들어지는 생성자
        Unit.__init__(self, name, hp)
        self.damage = damage

     def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name, location, self.damage))
    
     def damaged(self, damage):
         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
         self.hp -= damage
         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
         if self.hp <= 0:
             print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
              .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
       AttackUnit.__init__(self, name, hp, damage)
       Flyable.__init__(self, flying_speed)

#발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

#오버라이딩 (자식 클래스에서 정의한 메소드를 쓰고 싶을 때, 메소드를 새롭게 정의해서 사용)
