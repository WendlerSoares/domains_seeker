import sys

import dns.resolver


resolver = dns.resolver.Resolver()


try:
    with open ("Lista_subs_domain.txt", "r") as arq:
        subdominios = arq.read().splitlines()
except:
    print("lista nao encontrada")
    sys.exit()
    

for sudominio in subdominios:
        try:
            sub_alvo = "{}.{}".format(subdominio, alvo)
            resultados = resolver.resolve(sub_alvo, "A")
            for resultado in resultados:
                        print("{} -> {}".format(sub_alvo, resultado))
        except:
               pass

