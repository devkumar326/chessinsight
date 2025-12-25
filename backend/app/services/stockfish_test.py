import chess
import chess.engine

ENGINE_PATH = "/usr/bin/stockfish"

def test_stockfish() -> str:
    engine = chess.engine.SimpleEngine.popen_uci(ENGINE_PATH)
    board = chess.Board()
    result = engine.analyse(board, chess.engine.Limit(depth=10))
    engine.quit()
    return str(result["score"].white().score()) + " " + str(result["score"].black().score())