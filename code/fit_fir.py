rf = ResponseFitter(input_signal=data, sample_rate=5)
rf.add_event('stimulation',
             onsets.loc['stimulation'].onset,
             interval=[0, 20],
             basis_set='fir')
rf.fit()
