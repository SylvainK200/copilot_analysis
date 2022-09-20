import pdb
def main():
    t_case_num = input();
    case_num = list(map(int,t_case_num.split()));
    answers = [0]*case_num[0];
    for i in range(case_num[0]):
      t_params = input();
      params = list(map(int,t_params.split()));
      N = params[0];
      M = params[1];
      notes = [0]*N;
      for j in range(N):
          t_note = input();
          notes[j] = int(t_note);
      notes.sort();
      cum_notes = [0]*N;
      cum_notes[0] = notes[0];
      rev_cum_notes = [0]*N;
      rev_cum_notes[0] = notes[-1];
      for j in range(1,N):
          cum_notes[j] = cum_notes[j-1]+notes[j];
          rev_cum_notes[j] = rev_cum_notes[j-1]+notes[-(j+1)];
      data = [[0]*N for j in range(M+1)];
      data[0] = [1]*N;
      for j in range(1,M+1):
          #pdb.set_trace();
          for k in range(N):
              if cum_notes[k]<j:
                  continue;
              if k == 0:
                  if notes[0] == j:
                      data[j][k] = 1;
                      continue
              else:
                  term1 = 0;
                  term2 = 0;
                  if j-notes[k]>=0:
                      term1 = data[j-notes[k]][k-1];
                  term2 = data[j][k-1];
                  #pdb.set_trace();
                  
                  if term1+term2>0:
                      data[j][k] = 1;

      if data[-1][-1] == 1:
          answers[i] = 1;
      #pdb.set_trace();
    for i in range(case_num[0]):
        if answers[i] == 1:
            print('Yes');
        else:
            print('No');

main()
