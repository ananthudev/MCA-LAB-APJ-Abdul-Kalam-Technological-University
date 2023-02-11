function check()
{
	var question1=document.quiz.question1.value;
	var question2=document.quiz.question2.value;
	var question3=document.quiz.question3.value;
	var correct=0;
	if(question1=="patna")
	{
		correct++;
	}
	if(question2=="thiruvananthapuram")
	{
		correct++;
	}
	if(question3=="gandhinagar")
	{
		correct++;
	}
	if(correct==0)
	{
		
		alert("Study Well! your score is " + correct );
	}
	if(correct>0&&correct<3)
	{
		
		alert("Your score is " + correct );
	}
	if(correct==3)
	{
		
		alert("Great job your score is " + correct );
	}
	
}
