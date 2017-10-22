#define N 1000000
#define WORD_LENGTH sizeof(int) * 8

void setbit(unsigned int* bits, unsigned int i){
	bits[i / WORD_LENGTH] |= 1 << (i % WORD_LENGTH)
} 

int testbit(unsigned int* bits, unsigned int i){
	return bits[i/WORD_LENGTH] & (1 << (i % WORD_LENGTH)); 
}

unsigned int bits[N/WORD_LENGTH + 1];

int main_free(int* xs, int n){
	int i, len = N/WORD_LENGTH + 1£»
	for(i=0; i<len; ++i){
		bits[i] = 0;
	} 
	
	for(i=0; i<n; ++i){
		if(xs[i] < n){
			setbit(bits, xs[i]);
		}
	}
	
	for(i=0; i<=n; ++i){
		if(!testbit(bits, i)){
			return i;
		}
	}
}

int main(){
	main_free();
}
