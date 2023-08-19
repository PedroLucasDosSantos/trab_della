import argparse
import json
import csv
import time

def load_automaton(filename):
    with open(filename, 'r') as file:
        automaton = json.load(file)
    return automaton

def epsilon_closure(automaton, states):
    closure = set(states)
    for state in states:
        epsilon_transitions = automaton['transitions'].get(state, {}).get("", [])
        closure.update(epsilon_closure(automaton, epsilon_transitions))
    return closure

def run_test(automaton, test_input):
    current_states = [automaton['startState']]

    for symbol in test_input:
        next_states = []
        for state in current_states:
            transitions = automaton['transitions'].get(state, {}).get(symbol, [])
            epsilon_transitions = automaton['transitions'].get(state, {}).get("", [])
            next_states.extend(transitions)

            for epsilon_state in epsilon_transitions:
                next_states.extend(automaton['transitions'].get(epsilon_state, {}).get("", []))

        current_states = next_states

    return 'aceito' if any(state in automaton['acceptStates'] for state in current_states) else 'nao_aceito'


def main():
    parser = argparse.ArgumentParser(description='Simulador de autômatos finitos.')
    parser.add_argument('automaton_file', type=str, help='Arquivo contendo a representação do autômato.')
    parser.add_argument('test_input_file', type=str, help='Arquivo CSV contendo os testes de entrada.')
    parser.add_argument('output_file', type=str, help='Arquivo de saída para os resultados dos testes.')
    args = parser.parse_args()

    automaton = load_automaton(args.automaton_file)

    with open(args.test_input_file, 'r') as test_input_file, open(args.output_file, 'w', newline='') as output_file:
        test_reader = csv.reader(test_input_file, delimiter=';')
        result_writer = csv.writer(output_file, delimiter=';')

        result_writer.writerow(['Palavra de Entrada', 'Resultado Esperado', 'Resultado Obtido', 'Tempo de Execução'])

        for i, row in enumerate(test_reader):
            if i == 0:  # Ignorar a primeira linha (cabeçalhos das colunas)
                continue

            test_input = row[0]
            expected_result = int(row[1])  # Convertendo o resultado esperado para int

            start_time = time.time()
            result_obtained = run_test(automaton, test_input)
            end_time = time.time()
            execution_time = end_time - start_time

            result_writer.writerow([test_input, expected_result, result_obtained, execution_time])

if __name__ == "__main__":
    main()

