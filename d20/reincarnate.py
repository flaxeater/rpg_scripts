from random import choice
#
#d%	Incarnation	Str	Dex	Con
#01	Bugbear	+4	+2	+2
#02-13	Dwarf	+0	+0	+2
#14-25	Elf	+0	+2	-2
#26	Gnoll	+4	+0	+2
#27-38	Gnome	-2	+0	+2
#39-42	Goblin (Advanced Race Guide Goblin)	-2	+2	+0
#43-52	Half-elf	+0	+2	+0
#53-62	Half-orc	+2	+0	+0
#63-74	Halfling	-2	+2	+0
#75-89	Human	+0	+0	+2
#90-93	Kobold (Advanced Race Guide Kobold)	-4	+2	-2
#94	Lizardfolk	+2	+0	+2
#95-98	Orc (Advanced Race Guide Orc)	+4	+0	+0
#99	Troglodyte	+0	-2	+4
#100	Other (GM's choice)	?	?	?


table={
	(01):'Bugbear',
	(02,13):'Dwarf',
	(14,25):'Elf',
	(26):'Gnoll',
	(27,38):'Gnome	',
	(39,42):'Goblin ',
	(43,52):'Half,elf',
	(53,62):'Half,orc',
	(63,74):'Halfling',
	(75,89):'Human',
	(90,93):'Kobold',
	(94):'Lizardfolk',
	(95,98):'Orc',
	(99):'Troglodyte',
	(100):'Other',
}
print table
