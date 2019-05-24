# More on Key Andorid Aspects
- Activity,Service,Broadcast Receivers,Content Providers
- Intents,Bundle
- PackageManager
- Native Code 

# More on Activity
To start an activity
- startActivity(intent)
- intent can be either explicit or implicit
New : activityies can also get an "answer" / "result"

## Get replies from activities
A.X 
Intent i = new Intent(...);
int requestCode = 400;
startActivityForResult(i,requestCode);

B.Y
onCreate(){
	Intent resInt = new Intent();
	...
	setResult(Activity.RESULT_OK,resInt);
	finish();
}

----->
onActivityResult(int requestCode,int resultCode,Intent data){
	//check requestCode and resultCode
	...
}

# More on Service
- To start a service
	- Intent i = new Intent(...);
	- //intent MUST be an explicit intent(for security reasons)
	- startService(i)
- How to get back a reply?
	- 类似于 startActivityForResult
	- easiest is via vroadcast intents

# Services: The Full Story
- Three types of services:
	- Background
		不直接通知user，start with startService()，流程是startService()->S.onCreate()->S.onStartCommand()
	- Foreground
		用户是知道的，start with startService() + startForeground()(from the service's)，流程是startService()->S.onCreate()->S.onStartCommand()
	- Bound
		
