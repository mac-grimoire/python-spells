#!/usr/bin/env python3

def assign(v):
  print(f"Agssign: id(v)={id(v)}")
  v[0]="Marco Antonio"

def reassign(v):
  v=['Marco, Antonio','Carcano']
  print(f"Reagssign: id(v)={id(v)}")

v=['Marco','Carcano']

print(f"id(v)={id(v)}")
assign(v)
print(v)

reassign(v)
print(v)

print(f"id(v)={id(v)}")
