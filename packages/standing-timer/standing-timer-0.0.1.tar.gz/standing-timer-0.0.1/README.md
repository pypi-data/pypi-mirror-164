# Standing Timer

Simple Python app with a basic GUI for tracking how long I am standing per day.

## Deploy Steps

1. Install `twine`
2. Set your PyPi username to the `TWINE_USERNAME` environment variable
   - `export TWINE_USERNAME=\<your-user-name\>`
3. Set your PyPi password to the `TWINE_PASSWORD` environment variable
   - `export TWINE_PASSWORD=\<your-password\>`
4. Execute the deploy script
   - `sh deploy.sh`

## Future Improvements

- Improve the GUI
- Implement a FE/BE to analyze the results/show trends
