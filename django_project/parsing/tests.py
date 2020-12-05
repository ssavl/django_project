from django.test import TestCase
import json
# Create your tests here.

OBJ = """<div class="object" data-floatable="false" data-id="14" data-locked="false" data-scroll-effects="true" data-scroll-effects-class="fade" data-type="text" style="width: 531px; height: 320px; z-index: 4; left: 633px; top: 1089px;"><div class="content"><div class="editor"><p><span style="font-weight: 200; font-style: normal; font-size: 19px; font-family: tautz;">Сначала логотип был желанным, после финансового кризиса — неприличным. Еще вчера — ироничным, а сегодня — уже и не определишь. Словарная трактовка логомании имеет мало общего с тем, что подразумевают потребители моды. В справочнике Вебстера ближайший синоним — логорея, состояние, при котором речь становится чрезмерно многословной и несвязной. Короче говоря, пустословие.</span></p>
<p><span style="font-weight: 200; font-style: normal; font-size: 19px; font-family: tautz;"><br/></span></p>
<p><span style="font-weight: 200; font-style: normal; font-size: 19px; font-family: tautz;">В контексте современной моды такое определение звучит саркастически, учитывая, что логомания переживает третью, самую массовую волну.</span></p>
</div></div></div>"""

jsooon = dict(OBJ[])

print(type(jsooon))