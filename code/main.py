from settings import *
from support import *
from entities import *
from deck import *
from ui import UI
from powers import *
from timers import *
from time import sleep

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('slay the spire')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('Kreon-Regular.ttf', 30)
        self.running = True
        self.player_active = True

        # groups 
        self.all_sprites = pygame.sprite.Group()
        self.cards_group = pygame.sprite.Group()

        # data
        self.all_cards = card_folder_importer('images', 'cards')
        self.card = [Card(card, self.all_cards[card], self.cards_group) for card in list(self.all_cards.keys())]
        
        self.deck = Deck(self.all_cards, self.cards_group)
        self.player = Player(pygame.image.load(join('images', 'entities', 'ironclad.webp')).convert_alpha(), self.all_sprites)

        monster_name = choice(list(ENEMY_DATA.keys()))
        self.enemies = Enemies(monster_name, pygame.image.load(join('images', 'entities', f'{monster_name}.webp')).convert_alpha(), self.all_sprites)

        # timers
        self.timers = {'player_end': Timer(1000, func= self.opponent_turn), 'opponent_end': Timer(1000, func= self.player_turn) }

        # ui
        self.ui = UI(self.deck.hand_cards, self.player, self.enemies, self.cards_group, self.deck.draw_pile, self.deck.discard_pile, self.timers, self.apply_attack_card, self.apply_power_card, self.apply_skill_card)
        
        # cards
        self.deck.start_deck()

    def opponent_turn(self):
        enemy_name = self.enemies.name
        self.enemies.block = 0
        self.apply_enemy_attack(enemy_name)

        self.timers['opponent_end'].activate()

    def player_turn(self):
        if self.player.hp <= 0:
            sleep(0.5)
            self.running = False

        self.player.block = 0
        self.deck.draw()
        self.player_active = True

        for card in self.cards_group:
            card.rect.y = card.original_y

    def update_timer(self):
        for timers in self.timers.values():
            timers.update()

    def end_turn_button(self):
        turn_button = pygame.FRect(1100, 550, 120, 40)
        pygame.draw.rect(self.display_surface, COLORS['black'],turn_button)
        self.display_surface.blit(self.font.render('End Turn', True, (255,255,255)), (1100, 550))

        mouse_pos = pygame.mouse.get_pos()
        mouse_collide = turn_button.collidepoint(mouse_pos)

        if pygame.mouse.get_just_pressed()[0] and mouse_collide:
            self.timers['player_end'].activate()
            self.deck.discard_pile = self.deck.hand_cards[:]
            self.deck.hand_cards.clear()
            
    def apply_attack_card(self, player, target, card_name):

        card_data = CARDS_DATA.get(card_name)
        if not card_data:
            print(f"Erro: Carta '{card_name}' não encontrada!")
            return

        for effect in card_data['description']:
            action = effect[0]

            if action == 'deal':
                damage = effect[1]
                
                if damage == 'block':
                    damage = player.block
                else:
                    damage = int(damage)

                if target.block > 0:
                    absorbed = min(damage, target.block)
                    target.block -= absorbed
                    damage -= absorbed

                if damage > 0:
                    target.hp -= damage

        self.discard_card(card_name)

    def apply_skill_card(self, player, target, card_name):

        card_data = CARDS_DATA.get(card_name)
        if not card_data:
            print(f"Erro: Carta '{card_name}' não encontrada!")
            return

        for effect in card_data['description']:
            action = effect[0]

            if action == 'gain' and effect[2] == 'block':
                amount = eval(effect[1], {'self': self}) if isinstance(effect[1], str) else effect[1]
                player.block += amount

            elif action == 'draw':  
                amount = effect[1]
                self.deck.draw(amount)

        self.discard_card(card_name)

    def apply_power_card(self, player, target, card_name):
        card_data = CARDS_DATA.get(card_name)
        if not card_data:
            print(f"Erro: Carta '{card_name}' não encontrada!")
            return

        for effect in card_data['description']:
            action = effect[0]

            if action == 'apply':
                buff_amount = effect[1]
                buff_type = effect[2]
                player.apply_buff(buff_type, buff_amount)

        self.discard_card(card_name)

    def apply_enemy_attack(self, enemy_name):
        enemy_data = ENEMY_DATA.get(enemy_name)
        if not enemy_data:
            print(f"Erro: Inimigo '{enemy_name}' não encontrado!")
            return

        available_moves = list(enemy_data['moves'].values())
        attack_move = choice(available_moves)

        action = attack_move[0]
        value = attack_move[1]

        if action == 'deal':
            self.player.hp -= value

        elif action == 'gain' and attack_move[2] == 'block':
            self.enemies.block += value

    def discard_card(self, card_name):
        if self.ui.active_card:
            card_obj = self.ui.active_card
            if card_obj in self.deck.hand_cards:
                self.deck.hand_cards.remove(card_obj)
                self.deck.discard_pile.append(card_obj)

                card_obj.rect.topleft = (-100, -100)  
                self.ui.active_card = None

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update
            self.update_timer()
            self.all_sprites.update(dt)
            self.ui.update()

            # draw
            self.display_surface.blit(pygame.transform.scale(pygame.image.load(join('images', 'other', 'background.webp')).convert_alpha(),(WINDOW_WIDTH, WINDOW_HEIGHT)))
            self.all_sprites.draw(self.display_surface)
            self.end_turn_button()
            self.ui.draw()
            pygame.display.update()
        
        pygame.quit()
    
if __name__ == '__main__':
    game = Game()
    game.run()