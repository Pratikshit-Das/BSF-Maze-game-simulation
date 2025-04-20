
from flask import Flask, request, jsonify, render_template
from collections import deque

app = Flask(__name__)

FLOORS = 8
ROWS = 5
COLS = 5
MAX_HIGH_HAZARDS = 3
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.get_json()
    tower = parse_tower(data['tower'])
    reached, end_state, parent = bfs(tower)
    path = reconstruct_path(end_state, parent)
    return jsonify({'reached': reached, 'path': path})

def parse_tower(tower_data):
    parsed = []
    for floor in tower_data:
        floor_parsed = []
        for row in floor:
            floor_parsed.append([int(cell) if cell.isdigit() else cell for cell in row])
        parsed.append(floor_parsed)
    return parsed

def bfs(tower):
    queue = deque()
    visited = set()
    parent = {}

    start = (0, 2, 2, 0, False, False)
    queue.append(start)
    parent[start] = None

    while queue:
        floor, r, c, h3, has_key, has_manip = queue.popleft()
        current_state = (floor, r, c, h3, has_key, has_manip)

        if floor == FLOORS - 1:
            return True, current_state, parent

        visited.add(current_state)

        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                room = tower[floor][nr][nc]
                new_h3 = h3
                new_key = has_key
                new_manip = has_manip

                if room == 'L' and not has_key:
                    if has_manip:
                        new_manip = False
                    else:
                        continue

                if isinstance(room, int) and room == 3:
                    if h3 >= MAX_HIGH_HAZARDS:
                        if has_manip:
                            new_manip = False
                        else:
                            continue
                    else:
                        new_h3 += 1

                if room == 'K':
                    new_key = True
                if room == 'M':
                    new_manip = True

                new_state = (floor, nr, nc, new_h3, new_key, new_manip)
                if new_state not in visited:
                    queue.append(new_state)
                    parent[new_state] = current_state

        if tower[floor][r][c] == 'S' and floor + 1 < FLOORS:
            new_state = (floor + 1, r, c, h3, has_key, has_manip)
            if new_state not in visited:
                queue.append(new_state)
                parent[new_state] = current_state

    return False, current_state, parent

def reconstruct_path(end_state, parent_map):
    path = []
    while end_state:
        floor, r, c, *_ = end_state
        path.append((floor, r, c))
        end_state = parent_map.get(end_state)
    return path[::-1]

if __name__ == '__main__':
    app.run(debug=True)
