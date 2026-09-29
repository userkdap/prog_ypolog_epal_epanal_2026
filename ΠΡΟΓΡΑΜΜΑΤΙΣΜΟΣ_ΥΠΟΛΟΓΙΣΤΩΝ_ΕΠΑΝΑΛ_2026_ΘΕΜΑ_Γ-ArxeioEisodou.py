##ΕΠΑΝΑΛΗΠΤΙΚΕΣ ΠΑΝΕΛΛΑΔΙΚΕΣ ΕΞΕΤΑΣΕΙΣ
##HMEΡΗΣΙΩΝ ΚΑΙ ΕΣΠΕΡΙΝΩΝ ΕΠΑΓΓΕΛΜΑΤΙΚΩΝ ΛΥΚΕΙΩΝ
##ΣΑΒΒΑΤΟ 26 ΣΕΠΤΕΜΒΡΙΟΥ 2026
##ΕΞΕΤΑΖΟΜΕΝΟ ΜΑΘΗΜΑ:
##ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ ΥΠΟΛΟΓΙΣΤΩΝ
##
##ΘΕΜΑ Γ
##Σε έναν διαγωνισμό πληροφορικής συμμετέχουν διαγωνιζόμενοι από διάφορα
##σχολεία. Κάθε διαγωνιζόμενος λύνει έξι (6) προβλήματα. Η βαθμολογία σε
##κάθε πρόβλημα είναι από 0 έως και 20. Η τελική βαθμολογία κάθε
##διαγωνιζόμενου είναι ο μέσος όρος των βαθμολογιών του.
##Να αναπτύξετε πρόγραμμα σε γλώσσα προγραμματισμού Python, το οποίο:
##Γ1. Για κάθε διαγωνιζόμενο:
##α. Να διαβάζει το όνομά του (μον. 1).
##β. Να διαβάζει τις βαθμολογίες που έλαβε στα έξι (6) προβλήματα και να
##τις εισάγει στη λίστα VATH (μον. 3).
##Η εισαγωγή δεδομένων τερματίζεται όταν αντί για όνομα δοθεί η λέξη “END”.
##Δεν απαιτείται έλεγχος εγκυρότητας.
##Μονάδες 4
##Γ2. Να υπολογίζει με τη βοήθεια της συνάρτησης ΜΟ του ερωτήματος Γ3
##την τελική βαθμολογία κάθε διαγωνιζόμενου και να την εμφανίζει στην
##οθόνη μαζί με το όνομά του.
##Μονάδες 3
##Γ3. Να υλοποιήσετε τη συνάρτηση ΜΟ που δέχεται μία λίστα αριθμών και
##επιστρέφει τον μέσο όρο τους.
##Μονάδες 6
##Γ4. Να εμφανίζει πόσοι διαγωνιζόμενοι είχαν τελική βαθμολογία πάνω από 18.
##Αν δεν υπάρχει κανείς να εμφανίζει κατάλληλο μήνυμα.
##Μονάδες 6
##Γ5. Να εμφανίζει τη μέγιστη βαθμολογία που πέτυχε κάποιος διαγωνιζόμενος
##στο πρώτο (1ο) πρόβλημα.
##Μονάδες 6
##Σημείωση: Θεωρήστε ότι υπάρχουν τουλάχιστον 2 διαγωνιζόμενοι.
##
def ΜΟ(VATH):
    athroisma = 0
    for vathmos in VATH:
       athroisma += vathmos 
    return athroisma/len(VATH)

PROVLIMATA = 6
PANW = 0
KATW = 20
ORIO = 18
SIMANTIKO = 1

onoma = ""
diagonizomenoi_panw_apo_orio = 0
meg_vathm = 0
    
try:
    INPUTFILENAME="diagonismos.txt"
    print("Ανάγνωση του αρχείου εισόδου...\n")
    with open(INPUTFILENAME, 'r', encoding="utf-8") as inputfile:
        while onoma != "END":
            VATH = []
            onoma = inputfile.readline().strip('\n').strip('\ufeff')
            print("Όνομα διαγωνιζόμενου: {}".format(onoma))
            if onoma == "END":
                print("Τερματισμός εισαγωγής δεδομένων")
            else:
                for provlima in range(1, PROVLIMATA+1):
                    vathmologia = ""
                    while not vathmologia.isdigit() \
                      or int(vathmologia) not in range(PANW, KATW+1):
                      vathmologia = inputfile.readline().strip('\n').strip('\ufeff')
                      print("Βαθμολογία διαγωνιζόμενου {} στο πρόβλημα {}: {}".format(onoma, provlima, vathmologia))
                    vathmologia = int(vathmologia)
                    VATH.append(vathmologia)
                    if provlima == SIMANTIKO:
                        if meg_vathm < vathmologia:
                            meg_vathm = vathmologia
                teliki_vathmologia = ΜΟ(VATH)
                print("Τελική βαθμολογία του διαγωνιζόμενου {}: {:.2f}".format(onoma, teliki_vathmologia))
                if teliki_vathmologia > ORIO:
                    diagonizomenoi_panw_apo_orio += 1
except Exception as err:
    print("Σφάλμα στην ανάγνωση του αρχείου εισόδου!", err)

print("Διαγωνιζόμενοι με τελική βαθμολογία πάνω από {}: ".format(ORIO), end="")
print(diagonizomenoi_panw_apo_orio if diagonizomenoi_panw_apo_orio > 0 else "Κανείς")
print("Μέγιστη βαθμολογία που πέτυχε κάποιος διαγωνιζόμενος στο πρώτο (1ο) πρόβλημα: {}".format(meg_vathm))
