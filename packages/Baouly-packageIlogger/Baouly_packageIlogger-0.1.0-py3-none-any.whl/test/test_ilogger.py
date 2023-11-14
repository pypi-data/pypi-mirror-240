import unittest
from ilogger.ilogger import log, get_logs
import os

class TestILogger(unittest.TestCase):

    def setUp(self):
        # Supprimer les fichiers de logs existants avant les tests
        error_log_path = "logs/error.log"
        warning_log_path = "logs/warning.log"

        if os.path.exists(error_log_path):
            os.remove(error_log_path)

        if os.path.exists(warning_log_path):
            os.remove(warning_log_path)

    def test_log_error(self):
        log("Test message d'erreur.", "ERROR")
        logs = get_logs("ERROR")
        self.assertIn("Test error message.", logs[0])

    def test_log_warning(self):
        log("Tester message d'avertissement.", "WARNING")
        logs = get_logs("WARNING")
        self.assertIn("Test warning message.", logs[0])

if __name__ == '__main__':
    unittest.main()
