# gawk -f order.awk ../build/complex.pdb ../build/rec.pdb > cons.pdb
# using FIELDWIDTHS as it may not have space between occupancy and b-factor
# noting the format after using FIELDWIDTHS
# gawk IS REQUIRED
#
BEGIN {
   kbt=0.0019872041*300
   pi2=3.14159*3.14159
   ff=8*kbt*pi2
   FIELDWIDTHS = "6 5 5 4 2 4 12 8 8 6 6 12"
}

NR==FNR {
   p[NR]=$0; p1[NR]=$1; p3[NR]=$3; nr[NR]=$6-0; res[nr[NR]]=$4; n1=NR;
   next
}
NR!=FNR {
   p3[NR]=$3; p4[NR]=$4; nr[NR]=$6-0; pf[NR]=$11; nt=NR;
   next
}

END {
   for(i=2;i<=n1;i++) {
      fcon[nr[i],p3[i]]=0.0
   }

   nres0=nr[n1+1]-1
   for(i=n1+1;i<=nt;i++) {
      nr[i]=nr[i]-nres0
      if(p4[i]==res[nr[i]] || (p4[i]==" HIS" && (res[nr[i]]==" HIE" || res[nr[i]]==" HID" || res[nr[i]]==" HIP"))) {
         if(pf[i]!=0 && pf[i]!="      " && pf[i]!="") {
            fcon[nr[i],p3[i]]=ff/pf[i]
         }
      }
   }

   for(i=2;i<=n1;i++) {
      nr[i]=nr[i]-0
      if (p1[i]=="ATOM  ") {
        printf("%s%6.2f\n",substr(p[i],1,60),fcon[nr[i],p3[i]])
      } else {
        printf("%s\n",p[i])
      }
   }
}
