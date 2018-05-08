class Solution(object):
	def romanToInt(self,s):
		a=b=c=d=e=f=g=h=k=l=m=n=p=0
		for i in range(3):
			if 'CM' in s:
				s = s.replace('CM','900',1)
				a += 900 
			if 'CD' in s:
				s = s.replace('CD','400',1)
				b += 400
			if 'XC' in s:
				s = s.replace('XC','90',1)
				c += 90
			if 'XL' in s:
				s = s.replace('XL','40',1)
				d += 40
			if 'IX' in s:
				s = s.replace('IX','9',1)
				e += 9
			if 'IV' in s:
				s = s.replace('IV','4',1)
				f += 4
			if 'M' in s:
				s = s.replace('M','1000',1)
				g += 1000
			if 'D' in s:
				s = s.replace('D','500',1)
				h += 500 
			if 'C' in s:
				s = s.replace('C','100',1)
				k += 100
			if 'L' in s:
				s = s.replace('L','50',1)
				l += 50 
			if 'X' in s:
				s = s.replace('X','10',1)
				m += 10
			if 'V' in s:
				s = s.replace('V','5',1)
				n += 5 
			if 'I' in s:
				s = s.replace('I','1',1)
				p += 1
			end = a+b+c+d+e+f+g+h+k+l+m+n+p
		return (end)
        