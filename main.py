def count_batteries_by_health(present_capacities):
  h=e=f=0
  for i in present_capacities:
    a=(100*i)/120
    if a>=80:
      h=h+1
    elif (a>63 and a<80):
      e=e+1
    else:
      f=f+1
  # rated_capacity=120
  # soh=[]
  # for i in range(present_capacities):
  #   soh=100*i/rated_capacity
  #   soh.append(soh)
  # health_counts= {
  #   "healthy": 0,
  #   "exchange": 0,
  #   "failed": 0
  # }
  # for  i in range(soh):
  #   if soh[i]>=80:
  #     health_counts["healthy"]+=1
  #   elif soh[i]>63 and soh[i]<80:
  #      health_counts["exchange"]+=1
  #   else:
  #     health_counts["failed"]+=1
  
    
    
  return {
    "healthy": h,
    "exchange": e,
    "failed": f
  }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 72]
  
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
