import os
import time
import subprocess
from datetime import datetime


def get_running_processes():
    """
    Εκτελεί την εντολή 'tasklist' των Windows και επιστρέφει
    μια λίστα με τα ονόματα των προγραμμάτων που τρέχουν.
    """
    # Εκτελούμε την εντολή συστήματος 'tasklist' κρυφά
    # Χρησιμοποιούμε κωδικοποίηση 'cp850' ή 'utf-8' για τα Windows
    try:
        output = subprocess.check_output("tasklist", shell=True).decode("cp850", errors="ignore")
    except subprocess.CalledProcessError:
        # Αν αποτύχει, δοκιμάζουμε εναλλακτική κωδικοποίηση
        output = subprocess.check_output("tasklist", shell=True).decode("utf-8", errors="ignore")

    processes = set()
    # Διαβάζουμε το αποτέλεσμα γραμμή-γραμμή
    lines = output.splitlines()

    # Παραλείπουμε τις πρώτες 3 γραμμές που είναι τίτλοι
    for line in lines[3:]:
        parts = line.split()
        if len(parts) > 0:
            # Το όνομα της διεργασίας είναι το πρώτο κομμάτι (π.χ. chrome.exe)
            proc_name = parts[0]
            processes.add(proc_name)

    return processes


def start_monitoring():
    print("=== SYSTEM WATCHDOG ENABLED ===")
    print("Καταγραφή αρχικής κατάστασης συστήματος...")

    # Παίρνουμε το αρχικό 'αποτύπωμα' του συστήματος
    known_processes = get_running_processes()
    print(f"Εντοπίστηκαν {len(known_processes)} διεργασίες.")
    print("Ο 'Σκοπός' παρακολουθεί για εισβολείς...\n")

    try:
        while True:
            # Περιμένουμε λίγο πριν τον επόμενο έλεγχο
            time.sleep(3)

            # Παίρνουμε την τρέχουσα κατάσταση
            current_processes = get_running_processes()

            # Βρίσκουμε αν υπάρχουν ΝΕΕΣ διεργασίες
            # (Τρέχουσες μείον Γνωστές)
            new_threats = current_processes - known_processes

            if new_threats:
                timestamp = datetime.now().strftime("%H:%M:%S")
                print(f"[{timestamp}] ⚠️ ΠΡΟΣΟΧΗ! Νέα διεργασία εντοπίστηκε:")
                for proc in new_threats:
                    print(f"   -> {proc}")

                # Ενημερώνουμε τη λίστα γνωστών για να μην χτυπάει συνέχεια για το ίδιο
                known_processes.update(new_threats)

            # Ελέγχουμε αν κάτι σταμάτησε (προαιρετικό)
            stopped = known_processes - current_processes
            if stopped:
                known_processes = current_processes  # Ανανέωση λίστας

    except KeyboardInterrupt:
        print("\nΟ 'Σκοπός' απενεργοποιήθηκε.")


if __name__ == "__main__":
    start_monitoring()