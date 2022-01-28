import os
import datetime
import dota2gsi


rosha_state = 1

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def print_ability(state, ability):
    clearConsole()
    print(f"spell cast: {ability.get('name')}\n"\
          f"level: {ability.get('level')}\n"\
          f"cooldown: {ability.get('cooldown')}\n"\
          f"mana left: {state.get('hero', {}).get('mana')}")

def game_state(last_state, state):
    clearConsole()
    global rosha_state
    time = state['map']['clock_time']
    rosha_solver(rosha_state)
    converted = datetime.timedelta(seconds=time)
    print(f"new state: {converted}\n"\
          f"rosha_state: {rosha_state}")

def main():
    server = dota2gsi.Server()
    server.on_update(game_state)
    server.on_ability_cast(print_ability)
    server.start()


if __name__ == '__main__':
    main()