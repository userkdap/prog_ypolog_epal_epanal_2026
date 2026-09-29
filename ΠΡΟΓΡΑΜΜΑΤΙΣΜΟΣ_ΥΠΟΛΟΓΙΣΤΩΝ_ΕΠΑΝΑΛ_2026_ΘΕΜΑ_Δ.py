##ΕΠΑΝΑΛΗΠΤΙΚΕΣ ΠΑΝΕΛΛΑΔΙΚΕΣ ΕΞΕΤΑΣΕΙΣ
##HMEΡΗΣΙΩΝ ΚΑΙ ΕΣΠΕΡΙΝΩΝ ΕΠΑΓΓΕΛΜΑΤΙΚΩΝ ΛΥΚΕΙΩΝ
##ΣΑΒΒΑΤΟ 26 ΣΕΠΤΕΜΒΡΙΟΥ 2026
##ΕΞΕΤΑΖΟΜΕΝΟ ΜΑΘΗΜΑ:
##ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ ΥΠΟΛΟΓΙΣΤΩΝ
##
##ΘΕΜΑ Δ
##Μία εταιρεία αξιολογεί δέκα (10) σαρωτές QR‐code προκειμένου να
##επιλέξει τους έξι (6) καλύτερους. Κάθε σαρωτής υποβάλλεται σε πέντε (5)
##δοκιμές σάρωσης. Σε κάθε δοκιμή η απόδοσή του βαθμολογείται με
##έναν ακέραιο αριθμό από το 0 έως και το 20. Η τελική βαθμολογία του
##σαρωτή προκύπτει από το άθροισμα των πέντε (5) βαθμολογιών του.
##Να αναπτύξετε πρόγραμμα σε γλώσσα προγραμματισμού Python, το οποίο:
##Δ1. Για κάθε σαρωτή:
##α. Να διαβάζει το όνομα του μοντέλου και να το καταχωρίζει στη λίστα ON
##(μον. 2).
##β. Να διαβάζει τις βαθμολογίες των πέντε (5) δοκιμών και να τις
##καταχωρίζει στη λίστα DOK. Δεν απαιτείται έλεγχος εγκυρότητας
##(μον. 3).
##γ. Να υπολογίζει την τελική βαθμολογία με χρήση της συνάρτησης
##YPOLOGISMOS που ορίζεται στο ερώτημα Δ2 και να την αποθηκεύει στη λίστα VATH
##(μον. 3).
##Μονάδες 8
##Δ2. Να υλοποιεί τη συνάρτηση YPOLOGISMOS η οποία δέχεται μία λίστα και
##επιστρέφει το άθροισμα των στοιχείων της.
##Μονάδες 4
##Δ3. Να υπολογίζει και να εμφανίζει το πλήθος των σαρωτών με τελική
##βαθμολογία τουλάχιστον 80.
##Μονάδες 4
##Δ4. Να εμφανίζει τα ονόματα των μοντέλων με τις έξι (6) υψηλότερες
##τελικές βαθμολογίες. Δεν υπάρχουν ισοβαθμίες.
##Μονάδες 9
##
def YPOLOGISMOS(VATH):
    athroisma = 0
    for vathmos in VATH:
       athroisma += vathmos 
    return athroisma

SAROTES = 10
KALYTEROI = 6
DOKIMES = 5
PANW = 0
KATW = 20
ORIO = 80
            
ON = []
VATH = []

onoma = ""
sarotes_panw_apo_orio = 0

for montelo in range(1, SAROTES+1):
    DOK = []
    onoma = input("Όνομα μοντέλου {}: {}".format(montelo, onoma))
    ON.append(onoma)
    for dokimi in range (1, DOKIMES+1):
        vathmologia = ""
        while not vathmologia.isdigit() \
          or int(vathmologia) not in range(PANW, KATW+1):
          vathmologia = input("Βαθμολογία δοκιμής {} του μοντέλου {}: {}".format(dokimi, onoma, vathmologia))
        vathmologia = int(vathmologia)
        DOK.append(vathmologia)
    teliki_vathmologia = YPOLOGISMOS(DOK)
    VATH.append(teliki_vathmologia)
    print("Τελική βαθμολογία του μοντέλου {}: {}".format(onoma, teliki_vathmologia))
    if teliki_vathmologia >= ORIO:
        sarotes_panw_apo_orio += 1

print("Σαρωτές με τελική βαθμολογία τουλάχιστον {}: {}".format(ORIO, sarotes_panw_apo_orio))

##N = len(VATH)
##for i in range(N-1): # range(0, N–1, 1)
##    for j in range(N-1 , i , -1): # μέχρι και i–1
##        if VATH[j-1] < VATH[j]:
##            VATH[j-1], VATH[j] = VATH[j], VATH[j-1]
##            ON[j-1], ON[j] = ON[j], ON[j-1]

N = len(VATH)
isSorted = False
i = 1
while i < N and isSorted == False:
    isSorted = True
    for j in range(N-1, i-1, -1): # μέχρι και i–2
        if VATH[j-1] < VATH[j]:
            VATH[j-1], VATH[j] = VATH[j], VATH[j-1]
            ON[j-1], ON[j] = ON[j], ON[j-1]
            isSorted = False
    i += 1

print("Μοντέλα που επιλέγονται με τις έξι (6) υψηλότερες τελικές βαθμολογίες:")
print("--------------------------")
print("Μοντέλο\t\tBαθμολογία")
print("--------------------------")
for i in range(KALYTEROI):
    print("{}\t\t{}".format(ON[i], VATH[i]))
