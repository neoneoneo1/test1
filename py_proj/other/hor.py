dic={1980:'обеъзяна',1981:'курица',1982:'собака',1983:'свинья',1984:'крыса',1985:'бык',1986:'тигр',1987:'кролик',1988:'дракон',1989:'змея',1990:'лошадь',1991:'козел'}

while 1:
    date=raw_input('введите возраст или год рождения (-1 для выхода): ')
    if date=='-1':
        break;
    dat=int(date)
    vozrast=0
    date_rojd=0
    animal=''
    if dat<100:
        vozrast=dat
        date_rojd=2011-vozrast-1
        dat=date_rojd
        print dat
        while dat<1980:
            dat+=12
        while dat>1991:
            dat-=12            
        animal=dic.get(dat)
    else:
        vozrast=2011-dat-1
        date_rojd=dat
        while dat<1980:
            dat+=12
        while dat>1991:
            dat-=12            
        animal=dic.get(dat)
    print '\n'*20,'='*50,'\n',vozrast,'лет /',date_rojd,'год =',animal,'\n','='*50,'\n'    
print 'end'