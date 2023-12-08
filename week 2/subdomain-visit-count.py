class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        """
        1. create a dict{} to store every element of the cp domain
            the key == dom val = times
            use split() to only consider the second part
            use that dict{} to make another that has all of them
        2. add the val as we find them
        """
        #To store all the domain with their visit numbers
        domain = {}

        #Consider every string in the list cpdomain
        for cpdomain in cpdomains:
            dom_val, dom_name = cpdomain.split(" ")
            val = int(dom_val)

            #Add the domain name with val as its value
            if dom_name in domain:
                domain[dom_name] += val
            #Append on val if the domain name is already in domain
            else:
                domain[dom_name] = val

            #iterate through the name and add every domain name
            for i in range(len(dom_name)):
                if dom_name[i] == ".":
                    subdomain = dom_name[i + 1:]
                    
                    #check if it's already in domain
                    if subdomain in domain:
                        domain[subdomain] += val
                    
                    else:
                        domain[subdomain] = val
        
        #Make a formatted output list of type string
        result = ["{} {}".format(val, key) for key, val in domain.items()]

        return result
