# verificando Vlans
vlan_id = int(input("Ingrese el número de VLAN: "))

if 1 <= vlan_id <= 1005:
    print("La VLAN corresponde al rango normal.")
elif 1006 <= vlan_id <= 4094:
    print("La VLAN corresponde al rango extendido.")
else:
    print("El número de VLAN es inválido.")
