class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        num_sub_domains = {}
        cpsub_domain = []
        
        for cpdomain in cpdomains:
            count , domain = cpdomain.split(' ')
            len_domain = len(domain)
            count=int(count)
            
            if domain in num_sub_domains:
                num_sub_domains[domain]+=count
            else:
                num_sub_domains[domain]=count
                
            for i in range(len_domain):
                if domain[i] == ".":
                    sub_domain = domain[i+1:]
                    if sub_domain in num_sub_domains:
                        num_sub_domains[sub_domain] += count
                    else:
                        num_sub_domains[sub_domain] = count
                
        for sub_domain, count in num_sub_domains.items():
            temp_cpsub_domain = []
            temp_cpsub_domain.append(str(count))
            temp_cpsub_domain.append(sub_domain)
            temp_cpsub_domain = ' '.join(temp_cpsub_domain)
            cpsub_domain.append(temp_cpsub_domain)
        return cpsub_domain
            
                