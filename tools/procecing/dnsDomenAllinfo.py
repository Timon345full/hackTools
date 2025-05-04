import dns.resolver
import whois

def gettingDnsDomain():
    target_domain = input("Ведите домен: ")
    record_types = ["A", "AAAA", "CNAME", 'MX', "NS", "SDA", "TXT"]
    resolver = dns.resolver.Resolver()

    for record_type in record_types:
        try:
            answer = resolver.resolve(target_domain, record_type)
        except dns.resolver.NoAnswer:
            continue
        print(f"{record_type} записи {target_domain}:")
        for rdata in answer:
            print(f"{rdata}")

def AllInfoDns():
    def is_registers(domain_name): 
        try:
            w = whois.whois(domain_name)
        except Exception:
            return False
        else:
            return bool(w.domain_name)

    domain_name = input()
    if is_registers(domain_name):
        whois_info = whois.whois(domain_name)
        print("Домен зарегистрирован: ", whois_info.whois.registrar)
        print("WHOIS сервер: ", whois_info.whois_server)
        print("Дата создания домена: ", whois_info.creation_date)
        print("Домен годен до: ", whois_info.expiration_date)
    else:
        print("Домен не зарегестрирован: ")