sent = "---у_РОССИИ_естЬ_тОЛЬко_дВа_союзнника_—_ЕЁ_АРМИЯ_и_фЛОт==="

print(sent.lstrip(sent[0:3:]).rstrip(sent[55::]).title().replace("_",
                                                                 " " "").replace(
    "Союзнника", "Союзника"))
